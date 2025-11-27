class Solution:
  def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
    total_area = 0
    
    # 1. Finding the bounding box coordinates
    min_x = float('inf')
    min_y = float('inf')
    max_a = float('-inf')
    max_b = float('-inf')
    
    # Using a set to "toggle" corners.
    corners = set()
    
    for x, y, a, b in rectangles:
      # Updating the bounding box
      min_x = min(min_x, x)
      min_y = min(min_y, y)
      max_a = max(max_a, a)
      max_b = max(max_b, b)
      
      # Updating the total area
      total_area += (a - x) * (b - y)
      
      # Updating/toggling the four corners of the current rectangle
      p1 = (x, y)
      p2 = (x, b)
      p3 = (a, y)
      p4 = (a, b)
      
      for p in [p1, p2, p3, p4]:
        if p in corners:
          corners.remove(p)
        else:
          corners.add(p)
    
    # Checking if I have exactly 4 unique corners
    if len(corners) != 4:
      return False
      
    # Checking if those 4 corners *are* the bounding box corners
    bounding_corners = {
      (min_x, min_y),
      (min_x, max_b),
      (max_a, min_y),
      (max_a, max_b)
    }
    if corners != bounding_corners:
      return False

    bounding_box_area = (max_a - min_x) * (max_b - min_y)
    
    return total_area == bounding_box_area