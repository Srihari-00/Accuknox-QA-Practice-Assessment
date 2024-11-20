import psutil  # Library for retrieving system information
import logging  # Library for logging messages

# Configure logging to store messages in a file
logging.basicConfig(filename='system_health.log', level=logging.INFO)

# Define threshold limits for system metrics
THRESHOLDS = {
    'cpu': 80,       # CPU usage threshold in percentage
    'memory': 80,    # Memory usage threshold in percentage
    'disk': 90       # Disk usage threshold in percentage
}

# Function to check and log system health
def check_system_health():
    # Retrieve current system metric values
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Log warnings if thresholds are exceeded
    if cpu_usage > THRESHOLDS['cpu']:
        logging.warning(f'High CPU usage: {cpu_usage}%')
    if memory_usage > THRESHOLDS['memory']:
        logging.warning(f'High Memory usage: {memory_usage}%')
    if disk_usage > THRESHOLDS['disk']:
        logging.warning(f'High Disk usage: {disk_usage}%')

# Execute the system health check
check_system_health()
