
file_name = input("Unesite ime datoteke ")

try:
    with open(file_name, 'r') as file:
        total_confidence = 0
        count = 0
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                try:
                    confidence = float(line.split(":")[1])
                    total_confidence += confidence
                    count += 1
                except ValueError:
                    print("Error", line)
        
        if count > 0:
            average_confidence = total_confidence / count
            print("Average X-DSPAM-Confidence:", average_confidence)
        else:
            print("X-DSPAM-Confidence nije pronaden u datoteci.")

except FileNotFoundError:
    print("Datoteka nije pronadena".format(file_name))
