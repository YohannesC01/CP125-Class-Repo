# Lab 02 Exercise 8: Bouncing Ball Simulation
# Write your code below:

def calculate_bounce_height(current_height):
    """Calculate next bounce height (80% of current)."""
    # TODO: Implement this function
    return current_height * 0.8

def is_ball_stopped(height):
    """Return True if height < 1, False otherwise."""
    # TODO: Implement this function
    if height < 1:
        return True
    else:
        return False

def simulate_bouncing_ball(start_height):
    """
    Simulate bouncing ball.
    Returns: (bounce_count, total_distance)
    """
    # TODO: Implement using calculate_bounce_height and is_ball_stopped
    bounces = 0 
    height = start_height
    total_distances = start_height
    current_height = start_height

    while not is_ball_stopped(height):
        distance = calculate_bounce_height(current_height)
        bounces += 1
        total_distances += 2 * distance

    return total_distances, bounces

# Test your code here
print("Testing Bouncing Ball Simulation...")
