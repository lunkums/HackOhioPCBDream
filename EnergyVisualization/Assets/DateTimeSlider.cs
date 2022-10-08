using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class DateTimeSlider : MonoBehaviour
{
    [SerializeField] private TMP_Text sliderHeader;

    private void Start()
    {
        Slider slider = GetComponent<Slider>();
        slider.minValue = 0;
        slider.maxValue = DataManager.Instance.NumOfDateTimes;
        slider.onValueChanged.AddListener(UpdateData);

        sliderHeader.text = DataManager.Instance.Now.ToString();
    }

    private void UpdateData(float value)
    {
        DataManager.Instance.DateTimeIndex = (int)value;
        BuildingManager.Instance.ReadjustBuildings();
        sliderHeader.text = DataManager.Instance.Now.ToString();
    }
}
