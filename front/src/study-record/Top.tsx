import { useEffect, useState } from 'react'
import { Settings } from '../settings'
import StudyRecordForm from './Form'
import StudyRecordList from './List'
import { StudyRecord } from './Types'


function StudyRecordTop() {
  const [studyRecords, setStudyRecords] = useState({
    totalCount: 0,
    studyRecords: [],
  }) // リストの状態を管理
  const [formData, setFormData] = useState<StudyRecord | undefined>(undefined)

  // 初期表示で保存済みのリストを API から取得
  useEffect(() => {
    refreshList()
  }, [])

  const refreshList = () => {
    // APIから最新のStudyRecordを取得してリストを更新する
    fetch(`${Settings.APIEndPoint}/study-records`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok.')
        }
        return response.json()
      })
      .then(data => {
        setStudyRecords({
          totalCount: data.total_count,
          studyRecords: data.study_records,
        })
        setFormData(undefined) // reset form.
      })
      .catch(error => console.error('Error fetching study records:', error))
  }

  const handleEdit = (data: StudyRecord) => {
    setFormData(data)
  }

  return (
    <>
      <StudyRecordForm
        initialData={formData}
        onSubmit={() => refreshList()} // Form送信後にリストをリフレッシュ
        onCancel={() => setFormData(undefined)}
      />
      <StudyRecordList
        data={studyRecords}
        onEdit={handleEdit}
        onChange={() => refreshList()}
      />
    </>
  )
}

export default StudyRecordTop
