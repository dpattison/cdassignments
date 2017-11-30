class patient(object):
    def __init__(self, pid, name, allergies):
        self.pid = pid
        self.name = name
        self.allergies = allergies
        self.bednumber = 0

class hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.available_beds = range(1, capacity+1)
        print self.available_beds 
    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Sorry " + patient.name + ", the hospital is full"
        else:
            self.patients.append(patient)
            self.available_beds.sort()
            patient.bednumber = self.available_beds.pop(0)
            print patient.name + " has been admitted to bed " + str(patient.bednumber)
        return self

dave = patient(1, "Dave", "none")
fred = patient(2, "Fred", "none")
mike = patient(3, "Mike", "none")
jimmy = patient(4, "Jimmy", "none")

mlk = hospital("MLK", 3)

mlk.admit(dave).admit(fred).admit(mike).admit(jimmy)



# Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full
# Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
