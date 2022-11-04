#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sys

#applicant object contain all the fields of an applicant
class Applicant:  
  def __init__(self, name, phone, country, program, status):
    self.name = name
    self.phone = phone
    self.country = country
    self.program = program
    self.status = status

#class maintaining records in the Hash table
class ApplicantionRecords:  
    def __init__(self):
        self.HashMod = 1021

    def initializeHash(self):
        self.HashTable = [None]*self.HashMod

    def HashId(self, input):
        return hash(input) % len(self.HashTable)

    def insertAppDetails(self, name, phone, country, program, status):
        retValue = False
        val = self.HashId(name)
        
        ap = Applicant(name, phone, country, program, status)
        if self.HashTable[val] == None:
            #if empty then store the record in hash table
            self.HashTable[val] = ap
            retValue = True            
        else:
            #linear probing
            i = val
            i = i + 1
            d = i%self.HashMod
            while d != val:
                d = i%self.HashMod
                if self.HashTable[d] == None:
                    self.HashTable[d] = ap
                    retValue = True
                    print("Linear Probing")
                    break
                elif self.HashTable[d].name == name:
                    #insert not possible as same name already there
                    break
                i = i + 1
        return retValue
    
    def updateAppDetails(self, name, phone, country, program, status):
        retValue = False
        updatedFields = ""
        val = self.HashId(name)
        ap = Applicant(name, phone, country, program, status)
        if self.HashTable[val] != None and self.HashTable[val].name == name:
            if self.HashTable[val].phone != ap.phone :
                updatedFields = updatedFields + "Phone "
            if self.HashTable[val].country != ap.country :
                updatedFields = updatedFields + "Country "
            if self.HashTable[val].program != ap.program :
                updatedFields = updatedFields + "Program "
            if self.HashTable[val].status != ap.status :
                updatedFields = updatedFields + "Status "
                
            self.HashTable[val].phone = ap.phone
            self.HashTable[val].country = ap.country
            self.HashTable[val].program = ap.program
            self.HashTable[val].status = ap.status
            retValue = True
        else:
            #linear probing
            i = val
            i = i + 1
            d = i%self.HashMod
            while d != val:                
                if self.HashTable[d] == None:
                    #hit None implies record not there
                    break
                elif self.HashTable[d] != None and self.HashTable[d].name == ap.name:
                    #record found
                    if self.HashTable[d].phone != ap.phone :
                        updatedFields = updatedFields + "Phone "
                    if self.HashTable[d].country != ap.country :
                        updatedFields = updatedFields + "Country "
                    if self.HashTable[d].program != ap.program :
                        updatedFields = updatedFields + "Program "
                    if self.HashTable[d].status != ap.status :
                        updatedFields = updatedFields + "Status "
                
                    self.HashTable[d].phone = ap.phone
                    self.HashTable[d].country = ap.country
                    self.HashTable[d].program = ap.program
                    self.HashTable[d].status = ap.status
                    retValue = True
                    break

                i = i + 1
                d = i%self.HashMod
        
        return updatedFields
    
    def memRef(self, Program, outFileHandler):
        localProg = Program.strip()
        localList = []
        for item in self.HashTable:
            if item != None and item.program == localProg :
                localList.append ("{0} / {1} / {2} / {3} / {4}\n".format(item.name, item.phone, item.country, item.program, item.status))
            
        if outFileHandler != None and len(localList) != 0 :
            fileOut.write("---------- Applicants for Computer Science ----------\n")
            for lst in localList:
                fileOut.write(lst)

        return localList
    
    def appStatus(self, outFileHandler):
        intRejected = 0
        intApproved = 0
        intApplied = 0
        
        for item in self.HashTable:
            if item != None and item.status == "Rejected" :
                intRejected = intRejected + 1
            
            if item != None and item.status == "Applied" :
                intApplied = intApplied + 1

            if item != None and item.status == "Approved" :
                intApproved = intApproved + 1
        
        if outFileHandler != None:
            fileOut.write("---------- Application Status ----------\n")
            fileOut.write("Applied: {0}\n".format(intApplied))
            fileOut.write("Rejected: {0}\n".format(intRejected))
            fileOut.write("Approved: {0}\n".format(intApproved))
            
        return (intApplied, intRejected, intApproved)

    def destroyHash(self):
        self.initializeHash()

    


# In[9]:


CollegeApplication = ApplicantionRecords()
ApplicantionRecords.initializeHash(CollegeApplication)

fileInsertNew = open("inputPS07.txt","r")
fileOut = open("outputPS07Q1.txt","a")

count = 0
lines = fileInsertNew.readlines();
for line in lines:
    data = line.split("/")
    if len(data) == 5:
        count = count + 1
        ApplicantionRecords.insertAppDetails(CollegeApplication, data[0].strip(), data[1].strip(), data[2].strip(), data[3].strip(), data[4].strip().replace("\n", ""))

if count != 0:
    fileOut.write("Successfully inserted {0} applications into the system\n".format(count))
    
fileUpdate = open("promptsPS07Q1.txt","r")
lines = fileUpdate.readlines();
for line in lines:
    tagFetch = line.split(":")
    if len(tagFetch) == 2 and tagFetch[0].strip() == "Update":       
        nameFetch = tagFetch[1].split("/")
        if len(nameFetch) == 5 :
            ret = ApplicantionRecords.updateAppDetails(CollegeApplication, nameFetch[0].strip(), nameFetch[1].strip(), nameFetch[2].strip(), nameFetch[3].strip(), nameFetch[4].strip().replace("\n", ""))
            if ret != "":
                fileOut.write("Updated details of {0}. {1}has been changed.\n".format(nameFetch[0].strip(), ret))
    elif len(tagFetch) == 2 and tagFetch[0].strip() == "Program":
        ApplicantionRecords.memRef(CollegeApplication, tagFetch[1].strip(), fileOut)
    elif line.strip()  == "appStatus":
        ApplicantionRecords.appStatus(CollegeApplication, fileOut)
    


# In[ ]:




