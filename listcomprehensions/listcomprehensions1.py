#!/usr/bin/python -tt
#Practicing with basic list comprehensions 
import sys

def num_double(num_list):
  new_list= [x*2 for x in num_list]
  return new_list

def even_string(num_list):
  new_list = [str(x) if x%2==0 else x for x in num_list]
  return new_list

def tuples(num_list1, num_list2):
  new_list= [(a, b) for a in num_list1 for b in num_list2]
  return new_list

def list_of_list(num_list1, num_list2):
  new_list= [[x,y] for x in num_list1 for y in num_list2]
  return new_list


def main():
  list_a = range(10)
  list_b = range(10)
  print 'double list'
  print num_double(list_a), '\n'
  print 'even string list' 
  print even_string(list_a), '\n'
  print 'tuples list' 
  print tuples(list_a, list_b), '\n'
  print 'list of lists' 
  print list_of_list(list_a, list_b), '\n'
  
if __name__ == '__main__':
  main()


