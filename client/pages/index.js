// pages/index.js

import Link from "next/link";

export default function Home() {
  return (
    <div>
      <h1>Welcome to Your Survey App</h1>
      <p>Click the button below to start the survey:</p>
      <Link href="/survey">HI</Link>
    </div>
  );
}
