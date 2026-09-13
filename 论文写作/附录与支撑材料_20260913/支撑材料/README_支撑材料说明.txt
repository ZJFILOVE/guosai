支撑材料阅读与复现说明

一、结果版本
第一问：q1_solution.py，单日费用 35,118.598589 元。
第二问：q2_fresh_20260912，334天费用 13,774,501.344207 元。
第三问：q3_revision_a_20260912，主策略 mask_111，费用 13,551,983.071633 元。
第四问：q4_independent_codex_20260912，4-2 主策略 A42，费用 14,505,015.50 元；4-3 主策略 A43_111，费用 14,275,233.10 元。
第二至四问统计期间为2025年2月1日至12月31日；1月为暖启动。末端库存不统一强制回到初始值。

二、文件说明
AI工具使用详情.pdf 为组委会指定名称的AI详情；AI使用说明.docx 为同内容可编辑文件。
源码/ 保留对应版本全部求解、导出、校验与相关绘图源码；不同问题按原相对目录关系组织。
结果/ 下五个result工作簿为交付表；第二、三问移除了重复的扩展明细页，保留表内值和公式不变，逐单元格对照记录见核验/Excel精简核验.json。没有舍弃数值精度。
结果/问题二至四/*.csv.xz 是完整十分钟主策略明细、日级汇总或调整账本的无损XZ压缩件；Python lzma.open可直接读取，也可用7-Zip解压。
核验/ 的历史记录已去除本机用户目录信息，仅作为原运行证据；不作为新计算时的签名文件。文件校验清单.json对应本次支撑包。
原始赛题及官方附件不重复放入支撑包。复现时需提供同一批官方输入；原始哈希见历史运行记录。

三、从零复现（以下命令是复现入口，本次材料整理没有重新跑全年）
先解压支撑包，在该目录执行：
python -X utf8 核验支撑包.py
python -X utf8 准备复现.py --data-dir "官方原始文件目录" --output "新建复现目录"
进入新建复现目录后，按以下顺序运行。第二、三问有版本依赖，须先生成上游预测和签名；第四问读取第二、三问输出并核验哈希。

1. 第二问原运行环境：Python 3.13.9，numpy 2.3.5、scipy 1.16.3、lightgbm 4.7.0、openpyxl 3.1.5，详见环境/requirements_q2.txt。建议独立虚拟环境安装，不修改全局依赖。
python -X utf8 代码/实验/q2_fresh_20260912/run_fresh.py
python -X utf8 代码/实验/q2_fresh_20260912/write_report.py
python -X utf8 代码/实验/q2_fresh_20260912/verify_delivery.py

2. 第三、四问原运行使用另一环境（numpy 2.5.2、scipy 1.18.1），详见环境/requirements_q34.txt。保留上一步生成的第二问数据，不重复覆盖或修改签名。
python -X utf8 代码/q1_solution.py
python -X utf8 代码/实验/q3_revision_a_20260912/check_engine.py
python -X utf8 代码/实验/q3_revision_a_20260912/run_q3.py
python -X utf8 代码/实验/q3_revision_a_20260912/deliver_q3.py
python -X utf8 代码/实验/q4_independent_codex_20260912/test_model.py
python -X utf8 代码/实验/q4_independent_codex_20260912/run.py --jobs 2
python -X utf8 代码/实验/q4_independent_codex_20260912/deliver.py --sensitivity
python -X utf8 代码/实验/q4_independent_codex_20260912/audit.py
可另运行 test_recovery.py 核验续跑行为。绘图补充脚本需要pandas与matplotlib。

上述顺序会重新生成未打包的预测缓存、全部策略数组、候选评分和检查点。它们均为程序中间产物；为控制体积不重复附送大型缓存。已提供主策略完整数值明细、全部对照的日级结果和敏感性结果。
不同科学计算库版本可能产生浮点或最优解选取差异，应以原环境和费用/约束容差核对，不能要求所有重跑输出文件的字节哈希相同。

四、提交前整合
论文附录取同目录外“论文尾部_声明参考文献附录.docx/PDF”，其中先给核心代码定位，再列完整源码，页码需接续最终正文。
现存第一二问论文PDF采用旧第二问结果，不能直接拼接后提交；需先把第二问正文、表格及图更新为本包版本，并补齐其余正文。
本包不含承诺书、编号页、软件安装包、虚拟环境、对话全量日志及旧版试验。
