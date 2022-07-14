import {
  ComponentProps,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { useState } from "react"

import Spinner from "./Spinner"

import {
  DEFAULT_IFRAME_FEATURE_POLICY,
  DEFAULT_IFRAME_SANDBOX_POLICY,
} from "./IFrameUtils"

interface StylishIframeProps extends ComponentProps {
  args: {
    src: string
    srcdoc: string
    width: number | string
    height: number | string
    scrolling: string
  }
}

const StylishIframe = ({ args }: StylishIframeProps) => {
  const { src, srcdoc: srcDoc, height, scrolling } = args

  const [loadingIframe, setLoadingIframe] = useState(true)

  return (
    <div
      style={{
        position: "relative",
        overflow: "hidden",
        width: "100%",
        height: height || "100%",
        backgroundColor: "#ffffff",
      }}
    >
      {loadingIframe && (
        <Spinner
          style={{
            height: "100%",
            width: "100%",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        />
      )}
      <iframe
        allow={DEFAULT_IFRAME_FEATURE_POLICY}
        style={{
          position: "absolute",
          top: 0,
          right: 0,
          bottom: 0,
          left: 0,
          width: "100%",
          height: "100%",
        }}
        src={src}
        srcDoc={srcDoc}
        scrolling={scrolling}
        sandbox={DEFAULT_IFRAME_SANDBOX_POLICY}
        title="stylish_iframe"
        onLoad={() => setLoadingIframe(false)}
      />
    </div>
  )
}

export default withStreamlitConnection(StylishIframe)
