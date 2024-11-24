# Azumi - Mission Control and Data Visualization Tool

### Overview
Azumi is a **GUI application** designed to simplify and standardize mission planning, execution, and real-time data interaction. Built with **kRPC** and powered by **Kore**, Azumi focuses on creating dynamic, reusable profiles and missions for space exploration and beyond.  

This tool is in the **early stages of development**, but its vision is to streamline mission control workflows and enhance the flexibility of interacting with telemetry and custom data.

![msn_selector](https://i.imgur.com/EPz9rfY.png)
![dashboard](https://i.imgur.com/w2BbD8N.png)

---

### Key Features
- **Dynamic Profiles**  
  Write reusable Python-based profiles for various operations, such as orbital maneuvers. Profiles are parameterized, allowing you to easily customize aspects like orbit altitude or inclination.  

- **Customizable Missions**  
  Use JSON to define specific missions that leverage existing profiles. Missions can be tailored to specific vehicles or payloads and include adjustable parameters, configured before launch.  

- **Real-Time Visualization**  
  Visualize telemetry data dynamically through graphs and labels. Monitor critical values such as PID parameters or distances to targets, enabling precision and adaptability during missions.  

- **Parameter Adjustment**  
  Modify mission-critical values, such as PID settings, directly within the app during execution for fine-tuned control.

---

### Workflow
1. **Create Profiles**  
   Write Python scripts to define mission operations with adjustable parameters.  

2. **Build Missions**  
   Define missions using JSON to customize profiles for specific scenarios, payloads, or vehicles.  

3. **Configure Pre-Launch**  
   Adjust parameters for multiple missions within the app before launching.  

4. **Visualize and Control**  
   Monitor telemetry and custom data in real time, making dynamic adjustments as needed.

---

### Current Status
Azumi is in the **early development phase** and serves as a foundation for building advanced mission control systems. Feedback and contributions are welcome to refine its capabilities and expand its features.  

Stay tuned for updates as Azumi evolves into a robust mission planning and data visualization tool.

---

**Note:**  
Azumi is built on **kRPC** and leverages the **Kore** library for modularity and scalability.
