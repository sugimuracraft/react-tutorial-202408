import StudyRecordItem from './Item'
import { StudyRecord, StudyRecords } from './Types'

interface ListProps {
  data: StudyRecords
  onEdit: (data: StudyRecord) => void
  onChange: () => void
}

function StudyRecordList({ data, onEdit, onChange }: ListProps) {
  const totalTime = data.studyRecords.reduce((sum: number, record: StudyRecord) => sum + record.time, 0)

  return (
    <div>
      <h1>Study Records</h1>
      <ul>
        {data.studyRecords.map(studyRecord => (
          <StudyRecordItem
            key={studyRecord.id}
            data={studyRecord}
            onEdit={onEdit}
            onChange={() => onChange()}
          />
        ))}
      </ul>
      <div>
        合計時間: {totalTime}
      </div>
    </div>
  )
}

export default StudyRecordList
