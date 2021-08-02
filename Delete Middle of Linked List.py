def deleteMid(head):
    itr=head
    c=0
    l=[]
    while itr:
        c=c+1
        l.append(itr.data)
        itr=itr.next
    itr=head
    count=c//2
    r=l[count]
    for i in range(count):
        if i==count-1:
            if itr.next.data==r:
                itr.next=itr.next.next
        itr=itr.next
    a=head
    return a
