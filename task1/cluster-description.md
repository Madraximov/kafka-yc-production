# Kafka Cluster Deployment in Yandex Cloud

## Overview
This document describes the deployment and configuration of a production-ready Apache Kafka cluster in Yandex Cloud.
The cluster was deployed using Yandex Managed Service for Apache Kafka and configured according to best practices for
replication, data retention, and schema management.

---

## Cloud Environment
- Cloud Provider: Yandex Cloud
- Service: Managed Service for Apache Kafka
- Region: ru-central1

---

## Kafka Cluster Configuration

### Brokers
- Number of brokers: 3
- Kafka version: 3.x
- Zookeeper: Managed by Yandex Cloud

### Hardware Resources (per broker)
- vCPU: 2
- RAM: 8 GB
- Disk type: SSD
- Disk size: 100 GB

This configuration provides sufficient resources for fault tolerance, replication, and moderate production workloads.

---

## Topic Configuration

### Topic: `orders-topic`
- Partitions: 3
- Replication factor: 3

### Retention and Cleanup Policies
- `cleanup.policy=delete`
- `log.retention.ms=604800000` (7 days)
- `log.segment.bytes=1073741824` (1 GB)

These settings ensure controlled disk usage and predictable data retention behavior.

---

## Schema Registry

Schema Registry is deployed as a separate service and used to manage Avro schemas for Kafka messages.

- Registry URL: http://localhost:8081
- Subject: `orders-value`
- Schema format: Avro

The schema file `order.avsc` is stored in the repository and registered in Schema Registry.

---

## Data Flow Validation

To verify the cluster functionality:
- A Kafka producer sends test messages to the `orders-topic`
- A Kafka consumer reads messages from the same topic
- Successful message delivery confirms correct cluster operation, replication, and schema usage

---

## Validation Commands

```bash
kafka-topics.sh --describe --topic orders-topic
curl http://localhost:8081/subjects
curl http://localhost:8081/subjects/orders-value/versions
