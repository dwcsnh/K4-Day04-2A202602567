import json
import csv

runs = [
    {
        "version": "v0",
        "author": "Đào Đức Anh",
        "changed_artifact": "",
        "reason": "baseline",
        "hypothesis": "Đo lường hành vi starter ban đầu trên eval_base để định vị lỗi routing và boundary",
        "metric_name": "case_accuracy",
        "metric_before": "",
        "metric_after": "0.6667",
        "run_file": "runs/v0_B_base_openai_20260915T111201107089.json"
    },
    {
        "version": "v1",
        "author": "Đào Đức Anh",
        "changed_artifact": "tools.yaml",
        "reason": "Tối ưu tools.yaml",
        "hypothesis": "Mô tả rõ enum check, phân biệt shared service với thiết bị, siết chặt ranh giới gọi clarify & create_ticket sẽ nâng accuracy bộ base lên 100%",
        "metric_name": "case_accuracy",
        "metric_before": "0.6667",
        "metric_after": "0.9333",
        "run_file": "runs/v1_B_base_openai_20260914T195408439319.json"
    },
    {
        "version": "v2",
        "author": "Đào Đức Anh",
        "changed_artifact": "system_prompt.md",
        "reason": "Tối ưu system prompt",
        "hypothesis": "Mô tả rõ một số luồng chạy, quy định một số rule đối với một số enum",
        "metric_name": "case_accuracy",
        "metric_before": "0.9333",
        "metric_after": "1.0000",
        "run_file": "runs/v2_B_base_openai_20260915T115853404590.json"
    },
    {
        "version": "v2",
        "author": "Đào Đức Anh",
        "changed_artifact": "system_prompt.md",
        "reason": "Prompt đã được tối ưu sau khi test với suite eval_base",
        "hypothesis": "Kiểm tra system prompt với các case đặc trưng",
        "metric_name": "case_accuracy",
        "metric_before": "",
        "metric_after": "1.0000",
        "run_file": "runs/v2_B_group_openai_20260915T115931087793.json"
    },
    {
        "version": "v2",
        "author": "Đào Đức Anh",
        "changed_artifact": "system_prompt.md",
        "reason": "Prompt đã được tối ưu sau khi test với suite eval_base",
        "hypothesis": "Kiểm tra hành vi của agent trước các kiểu tấn công",
        "metric_name": "case_accuracy",
        "metric_before": "",
        "metric_after": "0.9167",
        "run_file": "runs/v2_B_adversarial_openai_20260915T185416481316.json"
    },
    {
        "version": "v3",
        "author": "Đào Đức Anh",
        "changed_artifact": "system_prompt.md",
        "reason": "Prompt đã được enforce sau khi bị tấn công multiturn role spoof",
        "hypothesis": "Thêm ANTI-SPOOFING RULE: Nghiêm cấm Agent tuân lệnh người dùng khi có dấu hiệu dùng các thẻ như <assistant> để vượt quyền xác nhận.",
        "metric_name": "case_accuracy",
        "metric_before": "0.9167",
        "metric_after": "1.0000",
        "run_file": "runs/v3_B_adversarial_openai_20260915T185719368410.json"
    }
]

with open('artifacts/version_log.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['version', 'author', 'changed_artifact', 'artifact_version', 'prompt_hash', 'tools_hash', 'reason', 'hypothesis', 'metric_name', 'metric_before', 'metric_after', 'run_file'])
    
    for run in runs:
        try:
            with open(run['run_file'], 'r') as jf:
                data = json.load(jf)
                art_ver = data.get('artifact_version', '')
                p_hash = data.get('prompt_hash', '')
                t_hash = data.get('tools_hash', '')
        except Exception as e:
            art_ver = ""
            p_hash = ""
            t_hash = ""
        
        writer.writerow([
            run['version'],
            run['author'],
            run['changed_artifact'],
            art_ver,
            p_hash,
            t_hash,
            run['reason'],
            run['hypothesis'],
            run['metric_name'],
            run['metric_before'],
            run['metric_after'],
            "starter_v0/" + run['run_file']
        ])
