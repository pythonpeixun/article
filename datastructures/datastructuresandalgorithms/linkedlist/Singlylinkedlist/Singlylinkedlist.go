package Singlylinkedlist

import "fmt"

type Node struct {
	data int
	next *Node
}

type SLinkedList struct {
	head   *Node
	length int
}

func (l *SLinkedList) IsEmpty() bool {
	return l.length == 0
}

// 新创建单链表 增删改查

func (l *SLinkedList) AddHead(value int) {
	l.head = &Node{data: value, next: l.head}
	l.length++
}

func (l *SLinkedList) AddTail(value int) {
	newNode := &Node{value, nil}
	if l.head == nil {
		l.head = newNode
		return
	}
	currNode := l.head

	for currNode.next != nil {
		currNode = currNode.next
	}
	currNode.next = newNode
}

// 删除第一次出现该值的Node
func (l *SLinkedList) DeleteNode(value int) bool {
	currNode := l.head
	if l.IsEmpty() {
		fmt.Println("EmptyListError")
		return false
	}
	if value == l.head.data {
		l.head = l.head.next
		l.length--
	}
	for currNode.next != nil {
		if currNode.next.data == value {
			currNode.next = currNode.next.next
			l.length--
			return true
		}
		currNode = currNode.next
	}
	return false
}

func (l *SLinkedList) Traverse() {
	currNode := l.head
	if currNode == nil {
		return
	}
	for currNode.next != nil {
		fmt.Println(currNode.data)
		currNode = currNode.next
	}
}

func New() *SLinkedList {
	return &SLinkedList{}
}
