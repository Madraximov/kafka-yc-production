# Kafka in Production: Yandex Cloud Integration

## Project Overview
This project demonstrates a production-ready deployment of an Apache Kafka cluster in Yandex Cloud
and its integration with an external data processing system (Apache NiFi).

The work is completed as part of the course module
"Kafka in production and integration with Big Data ecosystems".

---

## Architecture

Kafka cluster is deployed using Yandex Managed Service for Apache Kafka.
Apache NiFi is used as an external system to generate and publish data into Kafka.

Components:
- Apache Kafka (3 brokers)
- Apache ZooKeeper (managed)
- Schema Registry
- Apache NiFi

---

## Task 1: Kafka Cluster Deployment

### Kafka Cluster Configuration
- Cloud provider: Yandex Cloud
- Service: Managed Service for Apache Kafka
- Number of brokers: 3
- Kafka version: 3.x

### Hardware Resources (per broker)
- vCPU: 2
- RAM: 8 GB
- Disk type: SSD
- Disk size: 100 GB

### Topic Configuration
- Topic name: `orders-topic`
- Partitions: 3
- Replication factor: 3
- Retention policy:
  - `cleanup.policy=delete`
  - `log.retention.ms=604800000` (7 days)
  - `log.segment.bytes=1073741824` (1 GB)

### Schema Registry
- Schema format: Avro
- Subject: `orders-value`
- Schema file: `schemas/order.avsc`

---

## Task 1 Validation

The following commands were used to validate the Kafka cluster:

```bash
kafka-topics.sh --describe --topic orders-topic
curl http://localhost:8081/subjects
curl http://localhost:8081/subjects/orders-value/versions
