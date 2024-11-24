import logging
import time
from typing import Any

import krpc
import krpc.client
import krpc.connection
from krpc.client import Client
from PySide6.QtCore import QObject, Qt, QThread, QTimer, Signal


class ConnectionThread(QThread):
    success = Signal(bool)
    invalid_scene = Signal(bool)
    start_check_scene_timer = Signal()

    def __init__(self, addr, rcp_port, stream_port, conn_name):
        super(ConnectionThread, self).__init__()
        self.addr = addr
        self.rcp_port = rcp_port
        self.stream_port = stream_port
        self.conn_name = conn_name

        self.invalid_scene_timer = QTimer()
        self.invalid_scene_timer.setInterval(3000)
        self.invalid_scene_timer.setSingleShot(True)
        self.invalid_scene_timer.timeout.connect(self.check_game_scene)

        self.start_check_scene_timer.connect(
            self.invalid_scene_timer.start, Qt.QueuedConnection  # type:ignore
        )

    def get_conn(self):
        return self.conn

    def run(self):
        try:
            self.conn = krpc.connect(
                name=self.conn_name,
                address=self.addr,
                rpc_port=self.rcp_port,
                stream_port=self.stream_port,
            )

            self.success.emit(True)
            self.check_game_scene()

        except Exception as e:
            print(e)
            self.success.emit(False)

    def check_game_scene(self):
        try:
            game_scene = self.conn.krpc.current_game_scene  # type:ignore
            if not game_scene == self.conn.krpc.GameScene.flight:  # type:ignore
                self.invalid_scene.emit(False)
                self.start_check_scene_timer.emit()

            else:
                self.invalid_scene.emit(True)
                self.deleteLater()

        except:
            self.invalid_scene.emit(False)
            self.start_check_scene_timer.emit()


class ConnectionModel(QObject):

    write = Signal(str)
    status = Signal(str)
    startup_finished = Signal(object)

    def __init__(self) -> None:
        super(ConnectionModel, self).__init__()
        self.log = logging.getLogger("azumi.connection")
        self.attempt_count = 0

        self.reconnect_timer = QTimer()
        self.reconnect_timer.setInterval(5000)
        self.reconnect_timer.setSingleShot(True)
        self.reconnect_timer.timeout.connect(self.reconnect_attempt)

        self.stored_addr = ""
        self.stored_rcp_port = 0
        self.stored_stream_port = 0
        self.stored_conn_name = ""

    def reconnect_attempt(self):
        self.connect_to_ksp(
            self.stored_addr,
            self.stored_rcp_port,
            self.stored_stream_port,
            self.stored_conn_name,
        )

    def connect_to_ksp(
        self,
        addr: str = "127.0.0.1",
        rcp_port_: int = 50000,
        stream_port_: int = 50001,
        conn_name: str = "azumi",
    ):

        if not self.stored_addr:
            self.stored_addr = addr
            self.stored_rcp_port = rcp_port_
            self.stored_stream_port = stream_port_
            self.stored_conn_name = conn_name

        self.connection_thread = ConnectionThread(
            addr, rcp_port_, stream_port_, conn_name
        )

        self.write.emit(f"attempting connection to [{addr}:{rcp_port_}]")

        self.connection_thread.start()
        self.connection_thread.success.connect(self.success_switch)
        self.connection_thread.invalid_scene.connect(self.invalid_game_scene)

    def success_switch(self, success):
        if success:
            self.write.emit(f"<b style='color:#badc58'>SUCESSFULL</b> connection")
            self.conn = self.connection_thread.get_conn()

            self.status.emit(
                f"<b style='color:#badc58'>•</b> {self.stored_addr}@{self.stored_conn_name}"
            )

            self.startup_finished.emit(self.conn)

        else:
            self.write.emit(
                f"<b style='color:#ff7979'>ERROR</b> connecting, trying again in 5s"
            )
            self.status.emit(
                f"<b style='color:#ff7979'>•</b> Error in the connection attempt !"
            )
            self.reconnect_timer.start()

    def invalid_game_scene(self, success):
        if not success:
            self.write.emit(
                f"<b style='color:#ffbe76'>WARN</b> INVALID SCENE, please launch your vehicle, trying again in 3s"
            )

            self.status.emit(
                "<b style='color:#ffbe76'>•</b> the game is not in the launch game scene !"
            )

        else:
            self.status.emit(
                f"<b style='color:#badc58'>•</b> {self.stored_addr}@{self.stored_conn_name}"
            )
