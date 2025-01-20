########## This exercise goes over ############

# Variables
# Operators
# Conditional Statements
# Lists
# Dictionaries
# Loops 

###############################################

# Define data science job roles and required skills
job_roles = [
    {'role': 'Data Analyst', 'skills': ['Python', 'SQL', 'Excel']},
    {'role': 'Data Scientist', 'skills': ['Python', 'R', 'Machine Learning', 'Deep Learning']},
    {'role': 'Machine Learning Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-Learn']},
    {'role': 'Data Engineer', 'skills': ['Python', 'Apache Spark', 'Hadoop', 'SQL']},
    {'role': 'Business Intelligence Analyst', 'skills': ['Python', 'SQL', 'Tableau', 'Power BI', 'Excel']},
    {'role': 'Quantitative Analyst', 'skills': ['R', 'Python', 'MATLAB', 'Statistics']},
    {'role': 'Operations Analyst', 'skills': ['Python', 'SQL', 'Data Visualization', 'Process Improvement']},
    {'role': 'Database Administrator', 'skills': ['SQL', 'Oracle', 'MySQL', 'Database Management']},
    {'role': 'AI Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Computer Vision']},
    {'role': 'Statistician', 'skills': ['R', 'SAS', 'Python', 'Statistical Modeling']}
]
# My skills
my_skills = ['Python', 'SQL', 'Excel']

# Determine which jobs you're qualified for 
qualified_roles = []

for job in job_roles:
    # Initialize qualified flag
    qualified = True
    # Go through each skill in the skills key
    for skill in my_skills:
        if skill not in job['skills']:
            qualified = False
            break
    if qualified:
        # Add the job dictionary to the qualified_jobs list
        qualified_roles.append(job['role'])

print(qualified_roles)
