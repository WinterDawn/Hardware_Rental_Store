from Customers import Casual, Business, Regular
#from Store import Store
from Tools import Tool, Painting, Concrete, Plumbing, Woodwork, Yardwork

def main():
    tool = Painting("aaa",123)
    print(tool.get_type())


if __name__ == '__main__':
    main()