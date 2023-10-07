def generate_pascals_triangle(n):
    # Initialize an empty list to represent Pascal's triangle.
    triangle = []
    
    # Iterate from 0 to n-1 to generate the first n rows of the triangle.
    for i in range(n):
        # Create a new row and add the first element, which is always 1.
        row = [1] if not triangle else [1]
        
        # For elements between the first and last (exclusive), calculate them based on the previous row.
        for j in range(1, i):
            # Each element in the middle of the row is the sum of the two elements above it.
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        # Add the last element, which is also always 1.
        row.append(1)
        
        # Append the row to the triangle.
        triangle.append(row)
    
    # Return the completed Pascal's triangle as a list of lists.
    return triangle
