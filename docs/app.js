(() => {
  const atlas = window.JEV_ATLAS || { projects: [], updated: "" };
  const all = atlas.projects || [];
  const $ = selector => document.querySelector(selector);
  const query = $("#query");
  const category = $("#category");
  const language = $("#language");
  const sort = $("#sort");
  const grid = $("#grid");
  const count = $("#count");
  const empty = $("#empty");
  const localeToggle = $("#locale-toggle");

  const copy = {
    en: {
      toggle: "中文",
      title: "Find the JEV projects<br><span>that have source evidence.</span>",
      intro: "An open-source map for developers. Search, filter, and understand where JEV makes the decision.",
      verified: "source-verified",
      domains: "application domains",
      evidence: "pinned source evidence",
      search: "Search repos, use cases, decision points, or tags…",
      allCategories: "All categories",
      allLanguages: "All languages",
      sortStars: "Most stars",
      sortName: "Name A–Z",
      sortCategory: "By category",
      projects: "projects",
      snapshot: "snapshot",
      empty: "No matching projects. Try another query or clear a filter.",
      decision: "Decision point:",
      unknownLanguage: "Language unknown",
      unknownLicense: "License unknown",
      evidenceLink: "View evidence ↗",
      footer: "Source verification is not a security audit or performance endorsement. The data and method are public.",
      catalog: "Full catalog",
      method: "Method",
      contribute: "Contribute",
      description: "Search and filter source-verified JEV projects on GitHub."
    },
    zh: {
      toggle: "EN",
      title: "找到 JEV 生态里<br><span>真正有源码证据</span>的项目。",
      intro: "面向开发者的开源项目地图。搜索、筛选，并理解 JEV 在哪里做出决策。",
      verified: "源码已核验",
      domains: "应用领域",
      evidence: "固定提交证据",
      search: "搜索仓库、用途、决策点或标签…",
      allCategories: "全部分类",
      allLanguages: "全部语言",
      sortStars: "最多星标",
      sortName: "名称 A–Z",
      sortCategory: "按分类",
      projects: "个项目",
      snapshot: "快照",
      empty: "没有匹配项目。换个关键词或清除筛选试试。",
      decision: "决策点：",
      unknownLanguage: "语言未知",
      unknownLicense: "许可证未知",
      evidenceLink: "查看证据 ↗",
      footer: "源码核验不等于安全审计或性能背书。数据与方法完全公开。",
      catalog: "完整目录",
      method: "方法",
      contribute: "贡献",
      description: "搜索和筛选 GitHub 上源码已核验的 JEV 项目。"
    }
  };

  const esc = value => String(value ?? "").replace(/[&<>'"]/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;"
  })[c]);
  const unique = key => [...new Set(all.map(p => p[key]).filter(Boolean))].sort((a, b) => a.localeCompare(b));
  let locale = new URLSearchParams(location.search).get("lang") === "zh" ? "zh" : "en";

  function option(value, label) {
    return `<option value="${esc(value)}">${esc(label)}</option>`;
  }

  function localizeControls() {
    const t = copy[locale];
    const categoryValue = category.value;
    const languageValue = language.value;
    const sortValue = sort.value || "stars";
    category.innerHTML = option("", t.allCategories) + unique("category").map(value => option(value, value)).join("");
    language.innerHTML = option("", t.allLanguages) + unique("language").map(value => option(value, value)).join("");
    sort.innerHTML = option("stars", t.sortStars) + option("name", t.sortName) + option("category", t.sortCategory);
    category.value = categoryValue;
    language.value = languageValue;
    sort.value = sortValue;
  }

  function applyLocale() {
    const t = copy[locale];
    document.documentElement.lang = locale === "zh" ? "zh-CN" : "en";
    document.querySelector('meta[name="description"]').content = t.description;
    $("#hero-title").innerHTML = t.title;
    $("#hero-copy").textContent = t.intro;
    localeToggle.textContent = t.toggle;
    query.placeholder = t.search;
    $("#toolbar").setAttribute("aria-label", locale === "zh" ? "项目筛选器" : "Project filters");
    $("#result-label").textContent = t.projects;
    $("#empty").textContent = t.empty;
    $("#footer-note").textContent = t.footer;
    $("#catalog-link").textContent = t.catalog;
    $("#catalog-link").href = `https://github.com/PeriodBLUE/jev-project-atlas/blob/main/${locale === "zh" ? "CATALOG.zh-CN.md" : "CATALOG.md"}`;
    $("#method-link").textContent = t.method;
    $("#method-link").href = `https://github.com/PeriodBLUE/jev-project-atlas/blob/main/${locale === "zh" ? "METHODOLOGY.zh-CN.md" : "METHODOLOGY.md"}`;
    $("#contribute-link").textContent = t.contribute;
    $("#contribute-link").href = `https://github.com/PeriodBLUE/jev-project-atlas/blob/main/${locale === "zh" ? "CONTRIBUTING.zh-CN.md" : "CONTRIBUTING.md"}`;
    $("#metrics").innerHTML = `
      <span class="metric"><strong>${all.length}</strong> ${t.verified}</span>
      <span class="metric"><strong>${new Set(all.map(p => p.category)).size}</strong> ${t.domains}</span>
      <span class="metric"><strong>100%</strong> ${t.evidence}</span>`;
    $("#updated").textContent = `${t.snapshot} ${atlas.updated}`;
    localizeControls();
    render();
  }

  function render() {
    const t = copy[locale];
    const needle = query.value.trim().toLocaleLowerCase();
    let projects = all.filter(p => {
      const haystack = [p.repo, p.category, p.summary_zh, p.summary_en, p.decision_point_zh, p.decision_point_en, ...(p.tags || [])].join(" ").toLocaleLowerCase();
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
    grid.innerHTML = projects.map(p => {
      const summary = locale === "zh" ? (p.summary_zh || p.summary_en) : (p.summary_en || p.summary_zh);
      const decision = locale === "zh" ? (p.decision_point_zh || p.decision_point_en) : (p.decision_point_en || p.decision_point_zh);
      return `
        <article class="card">
          <div class="card-head">
            <a class="repo" href="${esc(p.url)}" target="_blank" rel="noreferrer">${esc(p.repo)}</a>
            <span class="stars">★ ${Number(p.stars || 0).toLocaleString()}</span>
          </div>
          <span class="category">${esc(p.category)}</span>
          <p class="summary">${esc(summary || "—")}</p>
          ${decision ? `<p class="decision"><strong>${esc(t.decision)}</strong>${esc(decision)}</p>` : ""}
          <div class="meta">
            <span>${esc(p.language || t.unknownLanguage)}</span><span>${esc(p.license || t.unknownLicense)}</span>
            ${p.source_url ? `<a href="${esc(p.source_url)}" target="_blank" rel="noreferrer"><span>${esc(t.evidenceLink)}</span></a>` : ""}
          </div>
        </article>`;
    }).join("");
  }

  localeToggle.addEventListener("click", () => {
    locale = locale === "en" ? "zh" : "en";
    const url = new URL(location.href);
    if (locale === "zh") url.searchParams.set("lang", "zh");
    else url.searchParams.delete("lang");
    history.replaceState({}, "", url);
    applyLocale();
  });
  [query, category, language, sort].forEach(node => node.addEventListener("input", render));
  applyLocale();
})();
