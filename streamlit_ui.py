import streamlit as st
from Contract_Deployment import *

student_id = st.text_input("Enter the student's id")

if st.button('Get Student'):
    student_id = int(student_id)
    st.success(getStudents(student_id))


student_name = st.text_input("Enter the student's name")
student_age= st.text_input("Enter the student's age")
enrollment_status = st.text_input("Enter the student's enrollment status")
grades = st.text_input("Enter the student's grades")

if st.button('Add Student'):
    # student_name = str(student_name)
    # student_age = int(student_age)
    # enrollment_status = str(enrollment_status)
    # grades = int(grades)
    addstudents(student_name, student_age, enrollment_status, grades)
