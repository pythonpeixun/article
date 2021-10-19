package Singlylinkedlist

import (
	"testing"
)

func TestSLinkedList_IsEmpty(t *testing.T) {
	type fields struct {
		head   *Node
		length int
	}
	tests := []struct {
		name   string
		fields fields
		want   bool
	}{
		// TODO: Add test cases.
		{"TestCase1", fields{nil, 0}, true},
		{"TestCase2", fields{&Node{data: 2, next: &Node{3, nil}}, 2}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			l := &SLinkedList{
				head:   tt.fields.head,
				length: tt.fields.length,
			}
			if got := l.IsEmpty(); got != tt.want {
				t.Errorf("SLinkedList.IsEmpty() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSLinkedList_AddHead(t *testing.T) {
	type fields struct {
		head   *Node
		length int
	}
	type args struct {
		value int
	}
	tests := []struct {
		name   string
		fields fields
		args   args
	}{
		// TODO: Add test cases.
		{"TestCase1", fields{&Node{data: 1, next: &Node{data: 2, next: nil}}, 2}, args{3}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			l := &SLinkedList{
				head:   tt.fields.head,
				length: tt.fields.length,
			}
			l.AddHead(tt.args.value)
		})
	}
}
