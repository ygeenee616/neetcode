class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> m;
        for(int i=0;i<nums.size();i++){
            if(m.find(nums[i])!=m.end()) return true;
            else m.insert({nums[i],nums[i]});
        }
        return false;
    }
};