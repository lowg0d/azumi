import logging
import signal
import time
from abc import ABC, abstractmethod

import krpc
from krpc.client import Client
from PySide6.QtCore import QObject, QThread, QTimer, Signal, Slot

from .conn import ConnectionModel
from .vessel import VesselModel

VESSELS_PATH = "src.vessels"


class Mission(QThread):
    write = Signal(str)
    state = Signal(str)
    status = Signal(str)
    connected = Signal()

    conn: Client

    def __init__(self, data) -> None:
        super().__init__()
        self.log = logging.getLogger("azumi.activemsn")

        self.addr = "127.0.0.1"
        self.rcp_port = 50000

        self.data = data

    def run(self) -> None:
        success = self.connect_to_ksp()
        print(success)
        if not success or not isinstance(self.conn, Client):
            return

        self.ksc = self.conn.space_center
        self.active_vessel = self.ksc.active_vessel  # type:ignore

        self.parameters = "parameters"

        self.log.info("Connecting to vessel...")
        self.write.emit("Connecting to vessel...")
        self.vessel = VesselModel(self.active_vessel)
        self.write.emit(f"Active Vessel: <b>{self.vessel.name}</b>")

        self.write.emit("Performing prelaunch operations")
        self.prelaunch()

        self.write.emit("Prelaunch operations done, issues: <b>0</b>")
        self.write.emit("Perfoming mission execution")

        self.execute()
        self.write.emit("Mission execution finished")

    def connect_to_ksp(self):
        self.write.emit(f"attempting connection to [{self.addr}:{self.rcp_port}]")
        try:
            self.conn = krpc.connect(
                name="azumi",
                address="127.0.0.1",
                rpc_port=50000,
                stream_port=50001,
            )
            self.finished.connect(self.conn.close)
            self.connected.emit()

            self.write.emit(f"<b style='color:#badc58'>SUCESSFULL</b> connection")
            self.status.emit(f"<b style='color:#badc58'>•</b> {self.addr}@azumi")
            return True

        except Exception as e:
            self.log.error(f"Error connecting: {e}")
            self.write.emit(f"<b style='color:#ff7979'>ERROR</b> connecting, '{e}'")
            self.status.emit(
                f"<b style='color:#ff7979'>•</b> Error in the connection attempt !"
            )
            return False

    @abstractmethod
    def execute(self) -> None:
        self.log.warning("Execute Not Implemented")

    @abstractmethod
    def prelaunch(self) -> None:
        self.log.warning("Prelaunch Not Implemented")
