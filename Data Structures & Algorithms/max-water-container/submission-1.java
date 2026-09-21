class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxWater = 0;

        while (left < right) {
            // Width between the two pointers
            int width = right - left;
            
            // Height is limited by the shorter line
            int currentHeight = Math.min(heights[left], heights[right]);
            
            // Calculate current area
            int currentArea = width * currentHeight;
            
            // Update max water found so far
            maxWater = Math.max(maxWater, currentArea);

            // Move the pointer that points to the shorter line
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxWater;
    }
}
