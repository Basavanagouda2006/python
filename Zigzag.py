print('NAME: Basavanagouda.y', 'USN: 1AY24AI017')

def run_zigzag(num_asterisks):
    indentation = 0
    direction = 1  # 1 for increasing, -1 for decreasing
    while num_asterisks > 0:
        print(" " * indentation + "*")
        indentation += direction
        num_asterisks -= 1
        if indentation == 0 or indentation == 5:  # Adjust upper limit as needed
            direction *= -1

run_zigzag(50)
