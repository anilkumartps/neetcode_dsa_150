class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> nums_set;
        for(auto &i: nums)
            nums_set.insert(i);
        if(nums_set.size() == nums.size())
            return false;
        else 
            return true;
    }
};
