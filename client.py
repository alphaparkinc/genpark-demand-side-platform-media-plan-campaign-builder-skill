class DemandSidePlatformMediaPlanCampaignBuilderClient:
    def build_dsp_campaign(self, media_plan_budget_usd: float, flight_dates: dict) -> dict:
        items = [
            {"line_item": "CTV_Streaming_TV_Awareness", "budget_usd": round(media_plan_budget_usd * 0.4, 2), "pacing": "EVEN"},
            {"line_item": "Desktop_Display_Retargeting", "budget_usd": round(media_plan_budget_usd * 0.35, 2), "pacing": "ACCELERATED"},
            {"line_item": "In_Stream_Audio_Consideration", "budget_usd": round(media_plan_budget_usd * 0.25, 2), "pacing": "EVEN"}
        ]
        return {
            "generated_line_items": items,
            "total_allocated_budget_usd": media_plan_budget_usd,
            "frequency_cap": "3 impressions per user per 24 hours"
        }
