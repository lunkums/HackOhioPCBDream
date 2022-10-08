using UnityEngine;
using UnityEngine.UI;

public class ReadjustButton : MonoBehaviour
{
    private void Start()
    {
        GetComponent<Button>().onClick.AddListener(BuildingManager.Instance.ReadjustBuildings);
    }
}
