import { Theme } from "streamlit-component-lib"
import React, { CSSProperties } from "react"
import "./css/spinner.css"

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
      <div className="loading-spinner"></div>
    </div>
  )
}

export default Spinner
