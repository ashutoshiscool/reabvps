# Install tmate
!apt update
!apt install -y tmate

!tmate

# Keep the script running to avoid termination
import time
while True:
    time.sleep(100)
