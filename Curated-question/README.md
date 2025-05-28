## leetcode 程式範例介紹（以 704.binary search 為例）
題目會給定
``` python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
```
目的是為了展示各參數是什麼類型，提供更好的提示，因此與一般def功能一模一樣，如下：
``` python
class Solution:
    def search(self, nums, target):
```
## leetcode 題目這麼長，該如何閱讀？
* 先看第一段 → 理解要做什麼
* 找 input / output →  知道格式
* 看 example → 具體理解
* 忽略 custom judge → 那是測試使用的
* 抓取關鍵字（以 24. remove element 題為例）→ in-place, sorted, unique...
* 找限制條件 → in-place： 不能創造新陣列、順序可變： 可以重新排列元素
