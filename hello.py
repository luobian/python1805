'''1.在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。

请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
'''


#二分查找


def Find(target, array):

    # write code here
    for i in array:
        for x in i:
            if target == x:
                return True
            else:
                continue
    return False
a = []
for i in range(5):
    a.append([i])
    for y in range(1, 5):
        a[i].append(i + y)

print(Find(5,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
'''
2.请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
'''

def replaceSpace(s):
    # s1 = s.split(' ')
    # s2 = ('%20').join(s1)
    return s.replace(' ','%20')

print(replaceSpace('hello world'))

'''
3.
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]

a = []
b = [1, 3]
print(a+b)
