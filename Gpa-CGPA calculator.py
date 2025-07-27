import streamlit as st

# Grading scale
GRADING_SCALE = {
    'A': {'range': (91, 100), 'points': 4.00},
    'A-': {'range': (80, 90), 'points': 3.66},
    'B+': {'range': (75, 79), 'points': 3.33},
    'B': {'range': (71, 74), 'points': 3.00},
    'B-': {'range': (68, 70), 'points': 2.66},
    'C+': {'range': (64, 67), 'points': 2.33},
    'C': {'range': (61, 63), 'points': 2.00},
    'C-': {'range': (58, 60), 'points': 1.66},
    'D+': {'range': (54, 57), 'points': 1.33},
    'D': {'range': (50, 53), 'points': 1.00},
    'F': {'range': (0, 49), 'points': 0.00}
}

def calculate_grade(percentage):
    percentage = float(percentage)
    for grade, data in GRADING_SCALE.items():
        if data['range'][0] <= percentage <= data['range'][1]:
            return grade, data['points']
    return 'F', 0.00

def calculate_gpa(courses):
    total_grade_points = 0
    total_credits = 0
    for course in courses:
        grade_points = course['grade_points'] * course['credits']
        total_grade_points += grade_points
        total_credits += course['credits']
    return total_grade_points / total_credits if total_credits > 0 else 0

def main():
    st.title("GPA & CGPA Calculator")
    st.subheader("Made by Roshaan")
    st.write("Specially for SMIU Students.")
    
    # Initialize session state
    if 'all_courses' not in st.session_state:
        st.session_state.all_courses = []
    
    tab1, tab2 = st.tabs(["Semester GPA Calculator", "CGPA Calculator"])
    
    with tab1:
        st.header("Semester GPA Calculator")
        num_courses = st.number_input("Number of courses this semester", min_value=1, max_value=20, value=1)
        
        courses = []
        for i in range(num_courses):
            st.subheader(f"Course {i+1}")
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input(f"Course name {i+1}", key=f"name_{i}")
            with col2:
                credits = st.number_input(f"Credits {i+1}", min_value=0.5, max_value=5.0, value=3.0, step=0.5, key=f"credits_{i}")
            
            percentage = st.slider(f"Percentage obtained {i+1}", 0, 100, 70, key=f"percentage_{i}")
            
            grade, grade_points = calculate_grade(percentage)
            st.write(f"Grade: **{grade}** (Grade Points: {grade_points})")
            
            courses.append({
                'name': name,
                'credits': credits,
                'percentage': percentage,
                'grade': grade,
                'grade_points': grade_points
            })
        
        if st.button("Calculate Semester GPA"):
            semester_gpa = calculate_gpa(courses)
            st.success(f"Your Semester GPA is: **{semester_gpa:.2f}**")
            
            # Store this semester's courses for CGPA calculation
            st.session_state.all_courses.extend(courses)
    
    with tab2:
        st.header("CGPA Calculator")
        if st.session_state.all_courses:
            cgpa = calculate_gpa(st.session_state.all_courses)
            st.success(f"Your Cumulative GPA (CGPA) is: **{cgpa:.2f}**")
            
            st.subheader("All Courses Taken")
            for i, course in enumerate(st.session_state.all_courses, 1):
                st.write(f"{i}. {course['name']}: {course['percentage']}% ({course['grade']}) - {course['credits']} credits")
            
            if st.button("Clear All Data"):
                st.session_state.all_courses = []
                st.rerun()
        else:
            st.warning("No course data available. Calculate a semester GPA first.")

if __name__ == "__main__":
    main()