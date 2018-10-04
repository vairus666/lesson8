# test
package com.company;

import org.junit.Test;

import static org.junit.Assert.*;

public class CourseTest {
    private int N = 30; // объем курса
    private int n; //количество записавщихся на курс + в списке ожидания
    private Course cs = new Course(30);


    //1 состояние (Идет запись на курс)
    //Тест1. Добавляем студента на курс при условии что его там еще нет на выходе должны получить его в списке курса
    @Test
    public void studentAdd(){
        cs.enroll(1);
        assertTrue(cs.getEnrollmentList().contains(1));

    }
    //Тест2. Добавляем имеющевося студента на курс. Проверяем что размер списка курса и размер списка ожидания не изменился
    @Test
    public void thisstudentAdd(){
        cs.enroll(2);
        int sizeenroll1 = cs.getEnrollmentList().size();
        int sizewaitlist = cs.getWaitingList().size();
        cs.enroll(2);
        int sizeenroll2 = cs.getEnrollmentList().size();
        int sizewaitlist2 = cs.getWaitingList().size();
        assertEquals(sizeenroll1, sizeenroll2);
        assertEquals(sizewaitlist, sizewaitlist2);
    }
    //Тест 3. Удаление из списка если он есть в списке. заполняем курс удаляем известный id и проверяет его наличие в списке
    //еще на всякий случай его наличие в списке ожидания
    @Test
    public void unenrollstudent(){
        for(int i =0; i<N-1; i++){
            cs.enroll(i);
        }
        cs.unenroll(3);
        assertFalse(cs.getEnrollmentList().contains(3));
        assertFalse(cs.getWaitingList().contains(3));
    }
    //Тест 4. Удаление студента из списка если его там нет. Размер не должен измениться после удаления.
    //В списке ожидания его тоже не должно быть
    @Test
    public void unenrollnotexist(){
        for(int i =0; i<N-1; i++){
            cs.enroll(i);
        }
        int size1 = cs.getEnrollmentList().size();
        cs.unenroll(31);
        int size2 = cs.getEnrollmentList().size();
        assertEquals(size1, size2);
        assertFalse(cs.getWaitingList().contains(31));
    }
    //Проверка перехода из состояния 1 в сотояние 2. Курс заполнен на n=N-1 и студента еще нет на курсе.
    // Тест 5. Курс заполнен на n=N-1. При добаление еще одного курс будет полностью заполнен
    //При условии что на курс он еще записан не был

    @Test
    public void transition(){
        for(int i =0; i<N-1; i++){
            cs.enroll(i);
        }
        cs.enroll(30);
        assertTrue(cs.isFullyEnrolled());

    }
    //Состояние 2. Курс заполнен. N = n
    //Тест 1. enroll студента нет в списке. Он добавится в список ожидания и в списке курса его не будет
    @Test
    public void enrollExistList() {
        for (int i = 0; i < N; i++) {
            cs.enroll(i);
        }
        cs.enroll(30);
        assertTrue(cs.getWaitingList().contains(30));
        assertFalse(cs.getEnrollmentList().contains(30));
    }
    //Тест 2. Добавление студента в список курса его он там есть. В списке ожидания его быть не должно.
     @Test
    public void addExistStudent(){
         for (int i = 0; i < N; i++) {
             cs.enroll(i);
         }
         cs.enroll(29);
         assertFalse(cs.getWaitingList().contains(29));
     }
     //Тест 3. Удаление студента с курса если он там есть. В списке курса и в списке ожидания его быть не должно
        @Test
    public void unenrollstudent2(){
            for(int i =0; i<N; i++){
                cs.enroll(i);
            }
            cs.unenroll(3);
            assertFalse(cs.getEnrollmentList().contains(3));
            assertFalse(cs.getWaitingList().contains(3));
    }
    //Тест 4. Удаление студента с курса если его там нет. Размер не изменить не у курса не у списка ожидания
    @Test
    public void unenrollnotexist2(){
        for(int i =0; i<N; i++){
            cs.enroll(i);
        }
        int size1 = cs.getEnrollmentList().size();
        cs.unenroll(31);
        int size2 = cs.getEnrollmentList().size();
        assertEquals(size1, size2);
        assertFalse(cs.getWaitingList().contains(31));
    }
    //Переход в сотояние 3. Не содержащийся на курсе студент при его заполнености попадает в список ожидания
    //Тест 5. Заполняем курс добавляем еще 1 студента. Он должен появится в списке ожидания
    @Test
    public void transition2(){
        for(int i =0; i<N; i++){
            cs.enroll(i);
        }
        cs.enroll(30);
        assertTrue(cs.getWaitingList().contains(30));
    }
    //Состояние 3. Идет запись в курс ожидания
    //Test 1. Добаление в список ожидания при условии что он там есть. Размеры списка ожидания после второго
    // добавления этого же id не должны изменится
    @Test
    public void addwaitinglistexist(){
        for(int i =0; i<N; i++){
            cs.enroll(i);
        }
        cs.enroll(30);
        int s1 = cs.getWaitingList().size();
        cs.enroll(30);
        int s2 = cs.getWaitingList().size();
        assertEquals(s1, s2);
    }
    //Тест 2. Удаление из списка ожидания студента если его там нет. Размеры списка ожидания после удаления
    // не существующего элемента должны быть равны
    @Test
    public void removewaitlist(){
        for(int i =0; i<N+1; i++){
            cs.enroll(i);
        }
        int s1 = cs.getWaitingList().size();
        cs.unenroll(32);
        int s2 = cs.getWaitingList().size();
        assertEquals(s1, s2);
    }
    //Тест3. Добавление в список ожидания если его там нет. Добавляем в список ожидания и проверяем его наличие
    @Test
    public  void addwaitinglist(){
        for(int i =0; i<N+1; i++){
            cs.enroll(i);
        }
        assertTrue(cs.getWaitingList().contains(30));
    }
    //Тест 4. Удаление из списка ожидания если он там есть.(а) он просто удаляется из списка б)удаляется из списка
    // ожидания и попадает в списко курса когда там освободится место)
    //a)
    @Test
    public void deletewaitlist(){
        for(int i =0; i<N+8; i++){
            cs.enroll(i);
        }
        cs.unenroll(32);
        assertFalse(cs.getWaitingList().contains(32));
        assertFalse(cs.getEnrollmentList().contains(32));
    }
    //Б) заполняем список курса и список ожидания на несколько мест. Удаляем из списка курса людей(несколько или 1)
    // и верхний из списка ожидания перемещается на основной курс

    @Test
    public void deletewaitlist2(){
        for(int i =0; i<N+1; i++){
            cs.enroll(i);
        }
        cs.unenroll(21);
        assertTrue(cs.getEnrollmentList().contains(30));
        assertFalse(cs.getWaitingList().contains(30));
    }
}



package ru.ac.uniyar.testingcourse;

import org.junit.Test;

import static org.junit.Assert.*;
import static org.assertj.core.api.Assertions.*;
/*Класс для тестирования класса Course

Последовательно проверяем каждый метод используя граничные условия; Необходимо протестировать их для разных случаев:
    1. Идет запись на курс
    2. Курс полон
    3. Идет запись в список ожидания.
Комбинируем эти случаи с условиями:
    1. Студент есть в списках
    2. Студента нет в списке
И получаем следующий набор тестов, охватывающих различные случаи употребления методов.
Кроме того, рассматриваем некоторый набор стандартных тестов - например, пустота контейнера после создания,
* */
public class CourseTest {
    Course course = new Course(2);
    int student=0;

    @Test
    public void testThatNewEnrollmentListIsEmpty(){
        assertThat(course.getEnrollmentList()).isEmpty();
    }
    @Test
    public void testThatNewWaitingListIsEmpty(){
        assertThat(course.getWaitingList()).isEmpty();
    }
    @Test
    public void testThatEnrolledStudentsInTheEnrollmentList(){
        course.enroll(student);
        assertThat(course.getEnrollmentList()).contains(student);
    }
    @Test
    public void testThatAfterEnrollingMaxAmountOfStudentsNewStudentAddedInWaitingList(){
        course.enroll(1);
        course.enroll(2);
        course.enroll(student);
        assertThat(course.getWaitingList()).contains(student);
    }
    @Test
    public void testUnenrollFromEnrollmentList(){
        course.enroll(student);
        course.unenroll(student);
        assertThat(course.getEnrollmentList()).doesNotContain(student);
    }
    @Test
    public void testUnenrollFromWaitingList(){
        course.enroll(1);
        course.enroll(2);
        course.enroll(student);
        course.unenroll(student);
        assertThat(course.getEnrollmentList()).doesNotContain(student);
    }
    @Test
    public void testThatAfterDeletingStudentFromEnrollmentListStudentFromWaitingListEnrolled(){
        course.enroll(1);
        course.enroll(2);
        course.enroll(student);
        course.unenroll(1);
        assertThat(course.getEnrollmentList()).contains(student);
    }
    @Test
    public void testThatFullyEnrolledCourseIsFullyEnrolled(){
        course.enroll(student);
        course.enroll(1);
        assertThat(course.isFullyEnrolled()).isTrue();
    }
    @Test
    public void testThatNotFullyEnrolledCourseIsFullyEnrolled(){
        course.enroll(student);
        assertThat(course.isFullyEnrolled()).isFalse();
    }
    @Test
    public void testThatNotHasWaitingListWhenCourseIsNotFullyEnrolled(){
        course.enroll(student);
        assertThat(course.hasWaitingList()).isFalse();
    }
    @Test
    public void testThatNotHasWaitingListWhenCourseFullyEnrolledAndWaitingListIsEmpty(){
        course.enroll(student);
        course.enroll(1);
        assertThat(course.hasWaitingList()).isFalse();
    }
    @Test
    public void testThatHasWaitingListWhenCourseFullyEnrolledAndWaitingListIsNotEmpty(){
        course.enroll(student);
        course.enroll(1);
        course.enroll(2);
        assertThat(course.hasWaitingList()).isTrue();
    }
    @Test
    public void testThatAlreadyEnrolledStudentIsNotAddedInEnrollmentList(){
        course.enroll(student);
        course.enroll(student);
        assertThat(course.getEnrollmentList()).containsOnlyOnce(student);
    }
    @Test
    public void testThatAlreadyEnrolledStudentIsNotAddedInWaitingList(){
        course.enroll(1);
        course.enroll(2);
        course.enroll(student);
        course.enroll(student);
        assertThat(course.getWaitingList()).containsOnlyOnce(student);
    }
    @Test
    public void testUnenrollingNonExistingStdentFromEnrollmentList(){
        course.enroll(1);
        course.unenroll(student);
        assertThat(course.getWaitingList()).doesNotContain(student);
    }
}









