#Tyler Brady  Team file opener

# all hashtaged lines are a less effective way of running this program.
# names = []
# id_number =[]
# job_title =[]
# salary = []

with open("hr_system.txt") as hr_file:

    for lines in hr_file:
        lines = lines.split()
        name = lines[0]
        id = lines[1]
        job = lines[2]
        salary = float(lines[3]) / 24 
        if job.lower() == "engineer":
            salary += 1000
        print(f"{name} (ID: {id}), {job} - ${salary:.2f}")
    #     names.append(lines[0])
    #     id_number.append(lines[1])
    #     job_title.append(lines[2])
    #     salary.append(lines[3])
    
    # for n,i,j,s in zip(names,id_number,job_title,salary):
    #     s = float(s)/24
    #     if j.lower() == "engineer":
    #         s += 1000
    #     print(f"{n} (ID: {i:2}), {j} - ${s:.2f}")

# print(names)
# print(id_number)
# print(job_title)
# print(salary)