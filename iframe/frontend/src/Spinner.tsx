import { Theme } from "streamlit-component-lib"
import React, { CSSProperties } from "react"

interface SpinnerProps {
  style?: CSSProperties
  stTheme?: Theme
}

const Spinner = ({ style, stTheme }: SpinnerProps) => {
  return (
    <div
      style={{
        ...style,
      }}
    >
      <div
        className="loading-spinner"
        style={{
          border: "10px solid #f3f3f3",
          borderTop: "10px solid #383636",
        }}
      ></div>
    </div>
  )
}

export default Spinner
