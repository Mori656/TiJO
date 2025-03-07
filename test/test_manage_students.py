import unittest

import src.manage_students as ms
class ManageStudentsTestCase(unittest.TestCase):

    def test_add_student_should_add_student_to_list(self):
        print("*** add_student ***")
        # given
        mstudents = ms.StudentManagement()
        # when
        result = mstudents.add_student("62362","Maciek",20)
        # then
        self.assertEqual(result, True)  # add assertion here

    def test_update_student_should_change_student_info(self):
        print("*** update_student ***")
        # given
        mstudents = ms.StudentManagement()
        mstudents.add_student("34543","Michał",20)
        # when
        result = mstudents.update_student("34543","Michał",23)
        # then
        self.assertEqual(result, True)  # add assertion here

    def test_remove_student_should_remove_student_from_list(self):
        print("*** remove_student ***")
        # given
        mstudents = ms.StudentManagement()
        mstudents.add_student("64543","Bob",4)
        # when
        result = mstudents.remove_student("64543")
        # then
        self.assertEqual(result, True)  # add assertion here

    def test_add_grade_should_add_grade_to_list(self):
        print("*** add_grade ***")
        # given
        mstudents = ms.StudentManagement()
        mstudents.add_student("64543","Bob",40)
        # when
        result = mstudents.add_grade("64543","WF",4)
        # then
        self.assertEqual(result, True)  # add assertion here
    def test_avg_grades_should_count_avarage_grade_for_all_students_from_subject(self):
        print("*** avg_grades ***")
        # given
        mstudents = ms.StudentManagement()
        mstudents.add_student("54354","Mikołaj",25)
        mstudents.add_student("43443","Marcel",23)
        mstudents.add_grade("54354","WF",5)
        mstudents.add_grade("43443","WF",2)
        # when
        result = mstudents.avg_grades("WF")
        # then
        self.assertEqual(result, 3.5)  # add assertion here


if __name__ == '__main__':
    unittest.main()
