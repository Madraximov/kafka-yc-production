from confluent_kafka import Producer
import json

p = Producer({'bootstrap.servers': 'broker:9092'})

p.produce(
    'orders-topic',
    value=json.dumps({
        "order_id": "1",
        "user_id": "42",
        "amount": 100.5,
        "created_at": "2025-01-01"
    })
)
p.flush()
