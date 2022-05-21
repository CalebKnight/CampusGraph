# Iterator only returns value not the node object.
class DSALinkedListIterator():
    def __iter__(self):
            currNd = self.head
            while currNd is not None:
                yield currNd.getValue()
                currNd = currNd.getNext() 