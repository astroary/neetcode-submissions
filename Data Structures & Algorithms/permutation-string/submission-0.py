class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        s1_counts, s2_counts = {}, {}
        # count of chars in s1
        for char in s1:
            s1_counts[char] = s1_counts.get(char, 0) + 1
        # sliding thru s2
        for r in range(len(s2)):
            char_in = s2[r]
            s2_counts[char_in] = s2_counts.get(char_in, 0) + 1

            # REMOVE the character that is now too far to the left
            if r >= len(s1):
                char_out = s2[r - len(s1)]
                
                # If there's only one of that letter, delete it entirely
                if s2_counts[char_out] == 1:
                    del s2_counts[char_out]
                else:
                    s2_counts[char_out] -= 1

            # Step 5: Check if our current frame matches s1 exactly
            if s1_counts == s2_counts:
                return True

        return False


        
        

