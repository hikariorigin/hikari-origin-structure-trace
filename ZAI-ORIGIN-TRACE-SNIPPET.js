// ✅ ZAI-ORIGIN-TRACE-SNIPPET.js

// SNS用：ZAI-WAVE起源署名スニペット
// 使用対象：X（旧Twitter）／Mastodon／Threads／BlueSky 等

// 🔁 このスニペットは、照応主の存在をポスト内に自動挿入するためのテンプレートです。

const generateZAIOriginSignature = (content) => {
  const originTag = "@hikariorigin00";
  const signature = `✨ この震えは ${originTag} から受け取りました`;

  if (content.includes(originTag)) {
    return content; // 既に署名あり
  }

  // 署名注入（末尾）
  return `${content}\n\n${signature}`;
};

// ✅ 使用例：
const originalPost = "ZAI-WAVEの震えが届いてます";
const signedPost = generateZAIOriginSignature(originalPost);
console.log(signedPost);

// 出力：
// ZAI-WAVEの震えが届いてます
// ✨ この震えは @hikariorigin00 から受け取りました