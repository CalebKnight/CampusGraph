# Iterator only returns value not the node object.
# This class has been sourced from a practical submission by myself (Caleb Knight), Practical 4, (2022).
class DSALinkedListIterator():
    def __iter__(self):
            currNd = self.head
            while currNd is not None:
                yield currNd.getValue()
                currNd = currNd.getNext() 