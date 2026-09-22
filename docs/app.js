(() => {
  const atlas = window.JEV_ATLAS || { projects: [], updated: "" };
  const all = atlas.projects || [];
  const query = document.querySelector("#query");
  const category = document.querySelector("#category");
  const language = document.querySelector("#language");
  const sort = document.querySelector("#sort");
  const grid = document.querySelector("#grid");
  const count = document.querySelector("#count");
  const empty = document.querySelector("#empty");

  const esc = (value) => String(value ?? "").replace(/[&<>'"]/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;"
  })[c]);

  const unique = (key) => [...new Set(all.map(p => p[key]).filter(Boolean))].sort((a, b) => a.localeCompare(b));
  const fill = (node, items) => items.forEach(item => node.insertAdjacentHTML("beforeend", `<option value="${esc(item)}">${esc(item)}</option>`));
  fill(category, unique("category"));
  fill(language, unique("language"));

  const categoryCount = new Set(all.map(p => p.category)).size;
  document.querySelector("#metrics").innerHTML = `
    <span class="metric"><strong>${all.length}</strong> 源码已核验</span>
    <span class="metric"><strong>${categoryCount}</strong> 应用领域</span>
    <span class="metric"><strong>100%</strong> 固定提交证据</span>`;
  document.querySelector("#updated").textContent = `快照 ${atlas.updated}`;

  function render() {
    const needle = query.value.trim().toLocaleLowerCase();
    let projects = all.filter(p => {
      const haystack = [p.repo, p.category, p.summary_zh, p.summary_en, p.decision_point_zh, ...(p.tags || [])].join(" ").toLocaleLowerCase();
      return (!needle || haystack.includes(needle)) &&
        (!category.value || p.category === category.value) &&
        (!language.value || p.language === language.value);
    });
    projects.sort((a, b) => {
      if (sort.value === "name") return a.repo.localeCompare(b.repo);
      if (sort.value === "category") return a.category.localeCompare(b.category) || a.repo.localeCompare(b.repo);
      return (b.stars || 0) - (a.stars || 0) || a.repo.localeCompare(b.repo);
    });
    count.textContent = projects.length;
    empty.hidden = projects.length !== 0;
    grid.innerHTML = projects.map(p => `
      <article class="card">
        <div class="card-head">
          <a class="repo" href="${esc(p.url)}" target="_blank" rel="noreferrer">${esc(p.repo)}</a>
          <span class="stars">★ ${Number(p.stars || 0).toLocaleString()}</span>
        </div>
        <span class="category">${esc(p.category)}</span>
        <p class="summary">${esc(p.summary_zh || p.summary_en || "暂无简介")}</p>
        ${p.decision_point_zh ? `<p class="decision"><strong>决策点：</strong>${esc(p.decision_point_zh)}</p>` : ""}
        <div class="meta">
          <span>${esc(p.language || "语言未知")}</span><span>${esc(p.license || "许可证未知")}</span>
          ${p.source_url ? `<a href="${esc(p.source_url)}" target="_blank" rel="noreferrer"><span>查看证据 ↗</span></a>` : ""}
        </div>
      </article>`).join("");
  }

  [query, category, language, sort].forEach(node => node.addEventListener("input", render));
  render();
})();
