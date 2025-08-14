def parse_metrics(metrics: str):
    keys = [
        'timestamp',
        'usagetime',
        'delta_cpu_time',
        'cpu_usage',
        'rx_data',
        'tx_data'
    ]
    values = metrics.strip(';').split(':')
    try:
        parsed = {
            keys[i]: float(values[i]) if "." in values[i] else int(values[i]) 
            for i in range(len(keys))
        }
        return parsed
    except(ValueError, KeyError):
        return {}