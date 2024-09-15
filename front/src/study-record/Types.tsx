export type StudyRecord = {
  id: string
  title: string
  time: number
}

export type StudyRecords = {
  totalCount: number
  studyRecords: StudyRecord[]
}
