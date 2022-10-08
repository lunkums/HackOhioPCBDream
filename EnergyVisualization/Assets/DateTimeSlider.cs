using UnityEngine;
using UnityEngine.UI;

public class DateTimeSlider : MonoBehaviour
{
    private void Start()
    {
        Slider slider = GetComponent<Slider>();
        slider.minValue = 0;
        slider.maxValue = DataManager.Instance.NumOfDateTimes;
        slider.onValueChanged.AddListener(UpdateData);
    }

    private void UpdateData(float value)
    {
        DataManager.Instance.DateTimeIndex = (int)value;
        BuildingManager.Instance.ReadjustBuildings();
    }
}
