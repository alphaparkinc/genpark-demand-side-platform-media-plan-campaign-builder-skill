from client import DemandSidePlatformMediaPlanCampaignBuilderClient

def main():
    client = DemandSidePlatformMediaPlanCampaignBuilderClient()
    res = client.build_dsp_campaign(50000.0, {"start": "2026-08-01", "end": "2026-08-31"})
    print(f"Allocated Budget: ${res['total_allocated_budget_usd']}")
    print(f"Frequency Cap: {res['frequency_cap']}")
    print("Generated Line Items:")
    for item in res["generated_line_items"]:
        print(f"  [{item['line_item']}] Budget: ${item['budget_usd']} ({item['pacing']} pacing)")

if __name__ == "__main__":
    main()
