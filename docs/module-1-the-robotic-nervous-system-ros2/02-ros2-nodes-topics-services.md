---
sidebar_position: 2
---

# ROS 2 Nodes, Topics, and Services

## Overview

At the heart of every ROS 2 application lies a distributed communication system designed to manage complexity and enable modular development. This section introduces the fundamental building blocks of ROS 2: Nodes, Topics, and Services. Understanding these concepts is crucial for designing, implementing, and debugging any robotic system built with ROS 2, especially for complex platforms like humanoid robots where numerous processes must communicate seamlessly.

## Key Concepts

*   **Node**: An executable process that performs computation (e.g., a sensor driver, a motor controller, an AI algorithm).
*   **Topic**: A named bus over which nodes exchange messages (e.g., sensor data, command signals). Topics implement a publish-subscribe model.
*   **Message**: A data structure containing information exchanged over topics.
*   **Service**: A request-reply communication mechanism, used when a node needs to request a computation from another node and wait for a response.
*   **Client/Server**: In a service, one node acts as the client making the request, and another acts as the server providing the response.

## Learning Objectives

By the end of this section, you will be able to:
- Define what ROS 2 nodes, topics, and services are and their respective roles.
- Create and execute simple ROS 2 nodes in Python.
- Implement publishers and subscribers for topics to exchange data between nodes.
- Implement service clients and servers for request-reply communication.
- Utilize ROS 2 command-line tools to inspect and debug communication within a ROS 2 graph.

## Topics Covered

### ROS 2 Nodes

Nodes are the atomic units of computation in ROS 2. Each node is responsible for a specific task.
-   **Creating a Simple Node**: How to write a basic ROS 2 node in Python using `rclpy`.
-   **Node Lifecycle**: Understanding the different states a node can be in (unconfigured, inactive, active, finalized).
-   **Node Naming**: Best practices for uniquely identifying nodes within a ROS 2 graph.

### ROS 2 Topics (Publish/Subscribe)

Topics facilitate asynchronous, one-to-many communication. A node "publishes" messages to a topic, and any number of other nodes can "subscribe" to that topic to receive those messages.
-   **Message Types**: Exploring common ROS 2 message types (e.g., `std_msgs`, `sensor_msgs`, `geometry_msgs`).
-   **Creating a Publisher**: How to send data to a topic.
-   **Creating a Subscriber**: How to receive data from a topic.
-   **Quality of Service (QoS) Settings**: Configuring reliability, durability, and liveliness for topic communication.

### ROS 2 Services (Request/Reply)

Services provide a synchronous, one-to-one communication mechanism where a "client" node sends a "request" to a "server" node and waits for a "response".
-   **Service Definitions**: Understanding how service types are defined (request and response message structures).
-   **Implementing a Service Server**: How to create a node that provides a service.
-   **Implementing a Service Client**: How to create a node that calls a service and processes the response.
-   **When to Use Services**: Differentiating between topics and services for different communication needs.

### ROS 2 Command-Line Tools

Effective use of ROS 2 involves a suite of command-line tools for introspection and debugging.
-   `ros2 run`: To execute a node.
-   `ros2 topic list`, `ros2 topic info`, `ros2 topic echo`: To inspect topics.
-   `ros2 service list`, `ros2 service call`: To inspect and call services.
-   `ros2 node list`: To inspect active nodes.