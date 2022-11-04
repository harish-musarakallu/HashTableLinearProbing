# HashTableLinearProbing
University requires help in developing a system to save details of students. They have received a lot of entries and need help retrieving details of their applicants quickly. Design a system that can quickly save and find the student details based on their name. The details are: Applicant Name,Phone,Country,Program Applied,Status. The Applicant details from the  database can be quickly be fetched/updated using the Hash table with Linear probing method

# Design
Create an Object in python representing the Applicant details 
class Applicant:  
  def __init__(self, name, phone, country, program, status):
    self.name = name
    self.phone = phone
    self.country = country
    self.program = program
    self.status = status

Create an Array list of Object Applicant of size N
HashTable [0]
HashTable [1]
HashTable [2]
HashTable [2]
.
.
.
HashTable [N-1]

When ever a New Applicant A1 details are given then use the Applicant “Name” and apply Hash function and do a Modulo of N to get the index of the array
Hash(A1.Name) % N => Index of the Hash table
HashTable [Hash(A1.Name) % N] = A1
It is also possible in a rare scenario that two applicant Names get the same Index. In this scenario do a Linear probing to find the next immediate slot index in the array and insert the details at that location
If  HashTable [Hash(A2.Name) % N] != Empty
{ 
  //Do a linear probing and find the next immediate slot in the array  and update the details of A2
}

# Timecomplexity
Insertion for the Best case = O(1)
In the best case the insertion is done by finding the Hash index to update the details
Insertion for the Worst case = O(N)
	In the worst case when the array is almost full, in this case linear probing has to be done for the entire HashTable to find the empty slot

Fetching for the Best case = O(1)
In the best case the fetching is done by finding the Hash index
Fetching for the Worst case = O(N)
In the worst case when the array is almost full, in this case linear probing has to be done for the entire HashTable to search for the Applicant name
