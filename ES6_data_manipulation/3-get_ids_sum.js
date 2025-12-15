export default function getStudentIdsSum (students) {
    if (!Array.isArray(students)) {
        return [];
    }
    return students.reduce((acc, students) => acc + students.id, 0);
}
